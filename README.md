# starvote

[STAR voting](https://www.starvoting.org/) is a
relatively-new ["electoral system"](https://en.wikipedia.org/wiki/Electoral_system)--a
method of running an election.  STAR Voting is simple--it's
simple to vote, and simple to tabulate.  And while a completely
fair and perfect electoral system is impossible,
STAR Voting's approach makes sensible tradeoffs
and avoids the worst pitfalls.  It's really great!

This module, **starvote**, implements a STAR Voting tabulator.
It requires Python 3.7 or newer, but also supports CPython 3.6.
(**starvote** relies on dictionaries preserving insertion order,
which is only guaranteed as of Python 3.7, but happened to work
in CPython 3.6.)

Features:

* Supports five
  [electoral systems](https://en.wikipedia.org/wiki/Electoral_system):

  - [STAR Voting](https://www.starvoting.org/star), the snazzy
    new single-winner voting system.
  - [Bloc STAR Voting](https://www.starvoting.org/multi_winner),
    a multiwinner variant of STAR voting that fills multiple
    seats with the *most popular* candidates.
  - [Allocated Score Voting](https://electowiki.org/wiki/Allocated_Score),
    a [proportional representation](https://en.wikipedia.org/wiki/Proportional_representation)
    electoral system, and so far the only such system officially
    authorized to be a "Proportional STAR Voting" method.
  - [Reweighted Range Voting](https://rangevoting.org/RRV.html)
    (aka "RRV"), an alternative proportional representation
    electoral system.  RRV isn't a STAR variant, but like STAR
    it's a form of
    [score voting.](https://en.wikipedia.org/wiki/Score_voting)
    So the ballot and instructions to the voter are identical
    to a STAR-PR election.  The RRV algorithm is much simpler
    than Proportional STAR Voting, and its "never discard a voter"
    approach is appealing.
  - [Sequentially Spent Score](https://electowiki.org/wiki/Sequentially_Spent_Score),
    a third variety of score-based proportional representation
    electoral system.


More info at: https://www.starvoting.us
Video: https://www.youtube.com/watch?v=3-mOeUXAkV0
