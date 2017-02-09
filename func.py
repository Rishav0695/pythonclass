def func(*args,**kwargs):
    print(args[0])
    print(kwargs['b'])
    print(args[1])
    print(kwargs['d'])
a=10
c=200
func(a,c,d='agarwal',b='rishav')#must be defined as in order arguments key argument#


