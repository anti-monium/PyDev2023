import cowsay
import argparse

def check(f, s):
    if f:
        return s
    return ''

pars = argparse.ArgumentParser()

pars.add_argument('-e', default='oo')
pars.add_argument('-f', default='default')
pars.add_argument('-l', default='', action='store_true')
pars.add_argument('-n', default='True', action='store_true')
pars.add_argument('-T', default='  ')
pars.add_argument('-W', default='40', type=int)

pars.add_argument('-b', default='', action='store_true')
pars.add_argument('-d', default='', action='store_true')
pars.add_argument('-g', default='', action='store_true')
pars.add_argument('-p', default='', action='store_true')
pars.add_argument('-s', default='', action='store_true')
pars.add_argument('-t', default='', action='store_true')
pars.add_argument('-w', default='', action='store_true')
pars.add_argument('-y', default='', action='store_true')

pars.add_argument('str', nargs='?')

args = pars.parse_args()

if args.l:
    l = sorted(cowsay.list_cows())
    print(*l)
else:
    preset = check(args.b, 'b') + check(args.d, 'd') + check(args.g, 'g') + check(args.p, 'p')
    preset += check(args.s, 's') + check(args.t, 't') + check(args.w, 'w') + check(args.y, 'y')
    cow = cowsay.cowsay(args.str,
            cow=args.f,
            preset=preset,
            eyes=args.e,
            tongue=args.T,
            width=args.W,
            wrap_text=args.n)
    print(cow)
