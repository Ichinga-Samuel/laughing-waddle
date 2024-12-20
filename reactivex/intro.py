from reactivex import Observable, from_iterable

# from_iterable reads from an iterable object
# returns an observable
obs = from_iterable(range(4))

# subscribe adds a function to work on the data
# the first is "on_next" for each data point
# "on_error" called once, when an error occurs
# "on_completed" called when data is completed
# subscribe can be called without any of these arguments
obs.subscribe(print)

r10 = from_iterable(range(10))
r10.subscribe(on_next=lambda x: print(f"another one {x}"),
              on_error=lambda: print("something went wrong"),
              on_completed=lambda: print("We are done here"))

r10r = Observable((range(10)))
print(type(r10r))
# r10r.subscribe(print) # subscribe won't work here, the input argument is not an observable
