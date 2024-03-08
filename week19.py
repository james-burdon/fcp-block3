import argparse
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt



def diff_eq(initial, t, alpha, beta, gamma, delta):
    dxdt = alpha * initial[0] - beta * initial[0] * initial[1]
    dydt = delta * initial[0] * initial[1] - gamma * initial[1]

    grad = [dxdt, dydt]

    return grad


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--initial', nargs='+', help="initial populations: 1st value is prey, 2nd value is predators",
                        default=[5, 5])
    parser.add_argument('--alpha', nargs='+', help="Up to 5 values for alpha", default=[0.1, 0.2, 0.3, 0.4, 0.5])
    parser.add_argument("--beta", type=float, default=0.1, help="value of beta")
    parser.add_argument("--delta", type=float, default=0.1, help="value of delta")
    parser.add_argument("--gamma", type=float, default=0.1, help="value of gamma")
    parser.add_argument("--save_plot", action='store_true', default=False,
                        help="--save_plot takes boolean values only. When present, must right 'True' 'and plot is saved")
    args = parser.parse_args()
    assert len(args.alpha) < 6, "Up to 5 values"
    initial = args.initial
    t_max = 100

    plot_eq(args.alpha, args.beta, args.gamma, args.delta, t_max, initial, args.save_plot)


def solve_eq(initial, t_max, alpha, beta, gamma, delta):
    '''
    Solves an SIR model using odeint.
    '''
    t = np.linspace(0, t_max, 1000)
    sir = odeint(diff_eq, initial, t, (alpha, beta, gamma, delta))
    return sir, t


def plot_eq(alpha, beta, gamma, delta, t_max, initial, save_plot):
    # fig = plt.figure()
    fig, axs = plt.subplots(len(alpha))
    for i in range(len(alpha)):
        model, t = solve_eq(initial, t_max, float(alpha[i]), beta, gamma, delta)
        # Plot the results
        axs[i].plot(t, model[:, 0], label='prey')
        axs[i].plot(t, model[:, 1], label='predators')
        axs[i].set_title(f'alpha = {alpha[i]}')
        axs[i].legend()
        axs[i].set_xlabel('Time')
        axs[i].set_ylabel('Population')
    plt.suptitle(f'Predator-Prey Populations: b = {beta}, y = {gamma}, d = {delta}\n\n',y=1)

    fig.tight_layout()

    if save_plot == False:
        plt.show()
    else:
        plt.savefig('Predator-Prey Populations')



if __name__ == '__main__':
    main()
