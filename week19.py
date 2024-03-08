import argparse
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# parser = argparse.ArgumentParser()
# parser.add_argument("--initial", type=int,
#                     help="initial population")
# parser.add_argument("-v", "--verbose", action="store_true",
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbose:
#     print(f"the square of {args.square} equals {answer}")
# else:
#     print(answer)




def diff_eq(initial, t, alpha, beta, gamma, delta):

    dxdt = alpha * initial[0] - beta * initial[0] * initial[1]
    dydt = delta * initial[0] * initial[1] - gamma * initial[1]

    grad = [dxdt, dydt]

    return grad


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--initial', nargs='+', help="initial populations: 1st value is prey, 2nd value is predators", default=[5,5])
    parser.add_argument('--alpha', nargs='+', help="Up to 5 values for alpha", default=[0.1,0.2,0.3,0.4,0.5])
    parser.add_argument("--beta", type=float,default=0.1,help="value of beta")
    parser.add_argument("--delta", type=float,default=0.1,help="value of delta")
    parser.add_argument("--gamma", type=float,default=0.1,help="value of gamma")
    parser.add_argument("--save_plot", type=bool,default=False,help="--save_plot takes boolean values only. When present, = True and plot is saved")
    args = parser.parse_args()
    assert len(args.alpha)<6, "Up to 5 values"
    initial=args.initial

    model, t = solve_eq(initial, t_max, alpha, beta, gamma, delta)
    # Plot the results
    plot_eq(t, model)

def solve_eq(initial, t_max, alpha, beta, gamma, delta):
    '''
    Solves an SIR model using odeint.
    '''
    t = np.linspace(0, t_max)
    sir = odeint(diff_eq, initial, t, (alpha, beta, gamma, delta))
    return sir, t





if __name__ == '__main__':
    main()
# parser.add_argument("-v", "--verbosity", action="count", default=0,
#                     help="increase output verbosity")
# answer = args.square**2
# if args.verbosity >= 2:
#     print(f"the square of {args.square} equals {answer}")
# elif args.verbosity >= 1:
#     print(f"{args.square}^2 == {answer}")
# else:
#     print(answer)