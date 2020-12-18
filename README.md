Creates Latex and HTML from a common JSON of course content.

JSON Formatting Example:
[
{
    "name": "Introduction to Vectors",
    "readings": [
        1.1,
        1.2,
        1.3
    ],
    "advice": [
        "The picture for problem 1.1 23 is on the previous page.",
        "The whole course is about linear combinations and vectors, don't slack off here.",
        "It might be a legit idea to do all the problems in this seciton.",
        "The other book chooses to delay discussions of dot products until very late. I personally believe this is a mistake.",
        "Do the worked out examples and try not to look at the solution key until you've actually worked on a problem for a bit.",
        "Answers don't count for much, explanations are where all the points are, so get used to writing out your thoughts for each step.",
        "You should be explaining at a level your fellows would understand.",
        "1.2 numbers 26 and 27 are meant to be a single problem.",
        "Problems 4 and 5 in 1.3 are the heart of the subject. Problem 4 is the 'Column multiplication picture' and problem 5 is the 'row multiplication picture'.",
        "For problem 7 in 1.3, the xs are unknown but fixed values, first assume that they aren't 0. After you're done, consider the possiblity that the xs in  are 0, is the conclusion wrong? ",
        "Hints for problems 4 and 5 from 1.3 can be found by reading 2.1."
    ],
    "work": {
        "1.1": "1, 3, 4, 6, 9, 11, 13, 18, 23, 26-29, and 31",
        "1.2": "1, 2, 6, 10, 13, 16, 20, 26/27 (these are a single problem), 29, 30 ",
        "1.3":"1, 2-6, 7, 14"
    }
},
{
    "name": "Systems and Elimination",
    "readings": [
        2.1,
        2.2,
        2.3
    ],
    "advice": [
        "The two pictures (column and row) in section 2.1 are the first step towards understanding the picture on the front of the book.",
        "They're two sides of the same thought, but seem very different.",
        "If you solve something using one of them consider trying it with the other. It won't always work, but it is good to consider.",
        "A matrix is a function. An $m\\times n$ matrix is a function from the n dimensional real numbers to the m dimensional real numbers.",
        "Elimination matricies are fairly tough, I'm keeping the assingments in 2.2 and 2.3 a little light.",
        "For number 20 in 2.2, to see the three planes described at the beginning, make a triangular tube out of a piece of paper.",
        "For number 32 in 2.2, you should use some ..., don't fill a page with numbers.",
        "The answer key answer for number 32 part d is describing the row and column spaces for the second matrix they describe in part c, not the first one.",
        "Problem 28 in section 2.3 is fairly tough to do without a hint, but it's really simple with one. For reference the 'associative law' is on page 61."
    ],
    "work": {
        "2.1":"1, 4-13, 15-17, 19, 20, 22, 26, 28, 31",
        "2.2":"3, 4-6, 11, 13, 20, 24, 32",
        "2.3":"1-3, 6, 7, 12, 13, 16, 17, 19, 24, 27, 28"
    }
}
]
