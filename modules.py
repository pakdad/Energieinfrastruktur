"""
A Brief Introduction to Python
Infrastrukturen Engineering
HafenCity Universität Hamburg (HCU)
The University Of The Built Environment And Metropolitan Development

Modul: BIW-M-211-100 Energie-Infrastructur
Instructors:
Prof. Dr.-Ing. Ingo Weidlich
Pakdad Pourbozorgi Langroudi
"""

def pipe_info(type, ID=10000000,  failure_event=''):
    """Display a pipe info."""
    if failure_event:
        description = f"This is a {type} pipe with the ID of {ID}.\nThe pipe is damaged on {failure_event}."
    else:
        description = f"This is a {type} pipe with the ID of {ID}."
    return description


def inventory_info(*pipes):
    """Print the list of pipes in inventory."""
    print("Generating a new inventory witht the following pipes:")
    for pipe in pipes:
        print(f"\t- {pipe}")


def network_profile(city, **network_info):
    """Build a dictonary containing everything we know about a network."""
    network_info['city'] = city
    return network_info