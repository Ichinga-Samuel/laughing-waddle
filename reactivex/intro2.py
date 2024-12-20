import sys

from reactivex import Observable, from_, compose, create, of, empty, create
from reactivex.operators import map, concat


def from_cli():
    # subscribe to the comand line arguments
    argv = from_(sys.argv[1:])
    argv.subscribe(print)


# operators
# operators transform observables and return new observables
# import them from reactivex.operators
# the pipe method of operators is used to compose multiple operators into an operation pipeline

def upper_case():
    # ascii character range for lowercase letters
    chars = range(97, 123)
    chars = from_(chars).pipe(map(lambda x: chr(x)), map(lambda x: x.upper()))
    chars.subscribe()


# new operators can be defined, by combining mutliple operators or defining a new logic
# this is done using compose

def upper_char():
    # compose here is simillar to pipe and can take multiple operators
    return compose(map(lambda x: chr(x).upper()))


def upper_case_2():
    from_(range(97, 123)).pipe(upper_char()).subscribe(print)


# create custom operators that return new observables
def lower():
    def _lower(source):
        def subscribe(observer, scheduler=None):
            def on_next(value):
                # main logic here
                # each value of the observable is worked on here
                observer.on_next(value.lower())
            return source.subscribe(
                on_next,
                observer.on_error,
                observer.on_completed,
                scheduler=scheduler,
            )
        return create(subscribe)
    return _lower


def lower_case():
    uppers = from_(range(97, 123)).pipe(upper_char())
    uppers.pipe(lower()).subscribe(print)



def only_third():
    def _only_third(source):
        def subscribe(observer, scheduler=None):
            def on_next(value):
                observer.on_next(chr(value)) if value % 3 == 0 else ...
            return source.subscribe(
                on_next,
                observer.on_error,
                observer.on_completed,
                scheduler=scheduler,
            )
        return create(subscribe)
    return _only_third



def third_letter():
    # chars = list(range(65, 91)) + range(97, 123)
    up = from_(range(65, 91))
    low = from_(range(97, 123))
    # res = from_(()).pipe(concat(up, low)) # this is correct
    # res = of().pipe(concat(up, low)) # this is correct
    res = empty().pipe(concat(up, low), only_third())
    res.subscribe(print)


# third_letter()


# create an observable
def first_five_chars(observer, scheduler):
    for i in range(10):
        observer.on_next(str(i))
    observer.on_completed()


def call_ffc():
    source = create(first_five_chars)
    source.subscribe(print)


call_ffc()
