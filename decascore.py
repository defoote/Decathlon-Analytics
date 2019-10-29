
import pandas as pd

events = ['m100', 'lj', 'sp', 'hj', 'm400', 'h110', 'dt', 'pv', 'jt', 'm1500']

A = [25.4347, 0.14354, 51.39, 0.8465, 1.53775, 5.74352, 12.91, 0.2797, 10.14, 0.03768]
B = [18, 220, 1.5, 75, 82, 28.5, 4, 100, 7, 480]
C = [1.81, 1.4, 1.05, 1.42, 1.81, 1.92, 1.1, 1.35, 1.08, 1.85]

coef = pd.DataFrame({'Event': events, 'A': A, 'B': B, 'C': C}).set_index('Event')


def score(event, mark):
    '''

    Calculates decathlon event scores.

    Parameters
    ----------
    event : string
        Abbreviation of event to calculate the score of.
        It must be one of 'm100', 'lj', 'sp', 'jh', 'm400', 'h110', 'dt', 'pv', 'jt', 'm1500'

    mark  : float
        Mark in specified event.
        - Running events in seconds
        - Throwing events in meters
        - Jumping events in centimeters

    Returns
    -------
    score : float
        The number of points scored in the event

    '''

    if type(mark) != float:
        return 0.0
    a = coef.loc[event]['A']
    b = coef.loc[event]['B']
    c = coef.loc[event]['C']
    score = int(a*(abs(b-mark))**c)
    return score
