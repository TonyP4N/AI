#!/usr/bin/env python3

# Task 1
def Travellers(List):
    from constraint import Problem, AllDifferentConstraint
    problem = Problem()
    people = ["claude", "olga", "pablo", "scott"]
    times = ["2:30", "3:30", "4:30", "5:30"]
    destinations = ["peru", "romania", "taiwan", "yemen"]
    t_variables = list(map(lambda x: "t_" + x, people))
    d_variables = list(map(lambda x: "d_" + x, people))
    problem.addVariables(t_variables, times)
    problem.addVariables(d_variables, destinations)
    problem.addConstraint(AllDifferentConstraint(), t_variables)
    problem.addConstraint(AllDifferentConstraint(), d_variables)

    # Claude is either the person leaving at 2:30 pm or the traveller leaving at 3:30 pm.
    problem.addConstraint(
        (lambda x: (x == "2:30") or
                   (x == "3:30")),
        ["t_claude"])

    # The person leaving at 2:30 pm is flying from Peru.
    for person in people:
        problem.addConstraint(
            (lambda x, y: ((y == "peru") and (x == "2:30")) or
                          ((y != "peru") and (x != "2:30"))),
            ["t_" + person, "d_" + person])

    # The person flying from Yemen is leaving earlier than the person flying from Taiwan.
    for person in people:
        for person2 in people:
            problem.addConstraint(
                (lambda x, y, z, m: (y != "yemen") or
                                    (m != "taiwan") or
                                    ((x == "2:30") and (z == "3:30")) or
                                    ((x == "2:30") and (z == "4:30")) or
                                    ((x == "2:30") and (z == "5:30")) or
                                    ((x == "3:30") and (z == "4:30")) or
                                    ((x == "3:30") and (z == "5:30")) or
                                    ((x == "4:30") and (z == "5:30"))),
                ["t_" + person, "d_" + person, "t_" + person2, "d_" + person2])

    # The four travellers are Pablo, the traveller flying from Yemen, the person leaving at 2:30 pm and the person
    # leaving at 3:30 pm.

    # Pablo is not flying from Yemen and is leaving at neither 2:30 nor 3:30;
    problem.addConstraint(
        (lambda x, y: (y != "yemen") and
                      (x != "2:30") and
                      (x != "3:30")),
        ["t_pablo", "d_pablo"])

    # whoever is flying from Yemen is likewise leaving at neither 2:30 nor 3:30.
    for person in people:
        problem.addConstraint(
            (lambda x, y: (y != "yemen") or
                          ((x != "2:30") and (x != "3:30"))),
            ["t_" + person, "d_" + person]
        )

    # add list to constraint
    for i in List:
        if i[1] == "peru" or i[1] == "romania" or i[1] == "taiwan" or i[1] == "yemen":
            problem.addConstraint(
                (lambda x: (x == i[1])),
                ["d_" + i[0]]
            )
        elif i[1] != "2:30" or i[1] != "3:30" or i[1] != "4:30" or i[1] != "5:30":
            problem.addConstraint(
                (lambda x: (x == i[1])),
                ["t_" + i[0]]
            )

    solns = problem.getSolutions()
    return solns


# Task 2
def CommonSum(n):
    cSum = n * (n ** 2 + 1) / 2
    return int(cSum)


# Task 3
def msqList(m, pairList):
    from constraint import Problem, AllDifferentConstraint, ExactSumConstraint

    problem = Problem()
    problem.addVariables(range(0, m * m), range(1, m * m + 1))
    problem.addConstraint(AllDifferentConstraint(), range(0, m * m))

    for row in range(m):
        problem.addConstraint(ExactSumConstraint(CommonSum(m)), [row * m + i for i in range(m)])

    for column in range(m):
        problem.addConstraint(ExactSumConstraint(CommonSum(m)), [column + m * i for i in range(m)])

    problem.addConstraint(ExactSumConstraint(CommonSum(m)), [dig_L + (m * dig_L) for dig_L in range(m)])

    problem.addConstraint(ExactSumConstraint(CommonSum(m)), [dig_R * (m - 1) + (m - 1) for dig_R in range(m)])

    # Accept parameter constraints
    for i in pairList:
        problem.addConstraint(ExactSumConstraint(i[1]), [i[0]])

    solns = problem.getSolutions()
    return solns


# Task 4
def pmsList(m, pairList):
    from constraint import Problem, AllDifferentConstraint, ExactSumConstraint

    problem = Problem()
    problem.addVariables(range(0, m * m), range(1, m * m + 1))
    problem.addConstraint(AllDifferentConstraint(), range(0, m * m))

    for row in range(m):
        problem.addConstraint(ExactSumConstraint(CommonSum(m)), [row * m + i for i in range(m)])

    for column in range(m):
        problem.addConstraint(ExactSumConstraint(CommonSum(m)), [column + m * i for i in range(m)])

    problem.addConstraint(ExactSumConstraint(CommonSum(m)), [dig_L + (m * dig_L) for dig_L in range(m)])

    problem.addConstraint(ExactSumConstraint(CommonSum(m)), [dig_R * (m - 1) + (m - 1) for dig_R in range(m)])

    # When the index is larger than m**2, transform it into the virtual square. Then reverse it to the original one.

    for Bdig_L in range(1, m):
        problem.addConstraint(ExactSumConstraint(CommonSum(m)), [((Bdig_L + i) % m) + (i * m) for i in range(m)])

    for Bdig_R in range(0, m-1):
        problem.addConstraint(ExactSumConstraint(CommonSum(m)), [((Bdig_R - i) % m) + (i * m) for i in range(m)])

    # Accept parameter constraints
    for i in pairList:
        problem.addConstraint(ExactSumConstraint(i[1]), [i[0]])

    solns = problem.getSolutions()
    return solns


# Debug
if __name__ == '__main__':
    print("debug run...")
