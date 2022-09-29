from random import randint

def splash():
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Biathlon".center(35))
    print("a hit or miss game".center(35))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    return None

def open():
    return 0

def closed():
    return 1

def is_open(target):
    if (target == open()):
        return True
    else:
        return False
    
def is_closed(target):
    if(target == closed()):
        return True
    else:
        return False
    
def new_targets():
    return [open(), open(), open(), open(), open()]

def close_target(target, targets):
    targets[target] = closed()
    return targets

def hits(targets):
    n = 0
    for x in targets:
        if is_closed(x) == True:
            n = n + 1
    return n

def target_to_string(target):
    if is_open(target) == True:
        return "* "
    else:
        return "0 "
        
def targets_to_string(targets):
    s = ""
    for x in targets:
       s = s + target_to_string(x)
    return s

def view_targets(targets):
    print()
    print("0 1 2 3 4")
    print()
    print(targets_to_string(targets))
    print()
    return None

def random_hit():
    n = randint(0,1)
    if n == 0:
        return True
    else:
        return False
    
def shoot(targets, target):
    n = random_hit()
    if n == True and is_open(targets[target]) == True:
        close_target(target, targets)
        return "Hit on open target"
    elif n == True and is_closed(targets[target]) == True:
        return "Hit on closed target"
    else:
        return "Miss"


