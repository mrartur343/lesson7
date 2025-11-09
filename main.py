#a = iter([0, 1, 5, 9])
#try:
#    print(next(a))
#    print(next(a))
#    print(next(a))
#    print(next(a))
#    print(next(a))
#    print(next(a))
#except:
#    print("!")


#class Counter:
#    def __init__(self):
#        self.i = 0
#    def __iter__(self):
#        self.i = 0
#        return self
#    def __next__(self):
#        self.i+=3+self.i
#        return self.i

#a = Counter()

#b =0

#while b<1000:
#    b = next(a)
#    print(b)

def generator(number, max_degree):
    i=0
    for _ in range(max_degree):
        yield number*i # Власну математичну дію
        i+=1
res = generator(2, 500)
print(res)
for a in res:
    print(a)


class Test:
    def __init__(self): # на додаткову оцінку, задавання атрибуту self.a при створені об'єкту цього класу
        self.a = 1 # своє початкове значення
    def __call__(self, *args, **kwargs):
        self.a*=2 # тут власна математична дія
        return self.a

test = Test()





print(test())
print(test())
print(test())
print(test())
print(test())


def checker(function):
    def checker(expression):
        try:
            result = function(expression)
        except Exception as exc:
            print(f"We have problems {exc}")
        else:
            print(f"No problems. Result – {result}")
    return checker

@checker
def calculate(expression):
    return eval(expression)
calculate("2+2")