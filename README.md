# bisb-bootcamp-2021-module09



## Before you begin
1. Make sure you have a GitHub account. See [here](https://www.codecademy.com/articles/f1-u3-git-setup) for help.
2. (Optional) You may want to cache your GitHub credentials in git so you do not repeatedly have to enter your
password. See [this page](https://docs.github.com/en/github/using-git/caching-your-github-credentials-in-git) for details.
3. Everyone will be assigned a number xx (e.g., 01-99)

## Brief Overview
This module will cover using git/GitHub to contribute to an existing body of code.

The major steps involved in this tutorial will be:

1. Forking someone else's repository
2. Creating a local copy of your fork
3. Implementing a feature on a new branch (including tests)
4. Opening a pull request for you new feature

## Activity Instructions
### Create a fork of this repository
A fork starts as a copy of another repository, but gives you administrative privileges,
so you can change the code and commit history however you like.

- Navigate to this repository: https://github.com/gwarmstrong/bisb-bootcamp-2021-module09
- Fork it (should fork to your github account)

  ![](images/fork-a-repo.png)
  
### Create a local copy of your fork
Having a local copy of a repository will let you make edits to the code and
commit history directly on your own machine.

- Clone the repository
```bash
$ GIT_USERNAME=<your-git-user-name-here>
$ git clone https://github.com/${GIT_USERNAME}/bisb-bootcamp-2021-module09.git
$ cd bisb-bootcamp-2021-module09
```
- Set the upstream remote (lets you pull code from the original owner's fork)
```bash
$ git remote add upstream https://github.com/gwarmstrong/bisb-bootcamp-2021-module09.git
```

- You can also install the python package in this directory at this time.
  The `-e` flag specifies "editable" mode, which means local changes you make
  to the python code in this package will be reflected when you import the
  module and run code.
```bash
$ pip install -e .
```

### Modifying the behavior of an existing feature in the repository
By this point, you should have been assigned a number `xx` for use during this activity.

In this section, you will modify the behavior of an existing feature in the repository.

Before making any changes, you should checkout a new branch with a name like `BRANCHNAME=git-tutorial`
```bash
$ git checkout -b $BRANCHNAME
```

There should be a file called `bootcamp_module09/core/student_${xx}.py`, with the following contents:

```python
def count_substring(string, substring):
    """Counts the number of occurrences of `substring` in `string`

    Parameters
    ----------
    string : str
        The string to count within
    substring : str
        The value to count in string

    Returns
    -------
    int
        The number of times `substring` occurs in `string`

    """
    count = 0

    string_length = len(string)
    substring_length = len(substring)
    n_subsequences = string_length - substring_length + 1

    for i in range(n_subsequences):
        left_bound = i
        right_bound = i + substring_length
        candidate_substring = string[left_bound:right_bound]
        if candidate_substring == substring:
            count += 1

    return count

```

And there should be corresponding tests in `bootcamp_module09/core/tests/test_student_${xx}.py`
```python
from bootcamp_module09.core.student_xx import count_substring


def test_count_substring_single():
    test_string = "CGCTAGCGT"
    test_substring = "TAG"

    expected_count = 1
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count


def test_count_substring_repeated():
    test_string = "AGCTAGCAGT"
    test_substring = "AGC"

    expected_count = 2
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count


def test_count_substring_none():
    test_string = "AGTCCCCTAGA"
    test_substring = "AAA"

    expected_count = 0
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count

```

**GOAL**: As a team we have decided that `count_substring` should be case insensitive, since `ACGT` is equivalent
to `acgt` for our DNA string use case.

For this portion of the activity, you should 
1. Write test cases that test whether the existing `count_substring` code is case insensitive.
2. Modify `count_substring` in your `student_xx.py` so that it is case insensitive (i.e., `'acgt' == 'ACGT', == 'aCgT'`).
3. Verify that your new code passes the unit tests you wrote. You can do that with the following (run from the root of the git repo):
    ```bash
    $ pytest
    ```
    If you do not have pytest installed, you can install it with
    ```bash
    $ pip install -U pytest
    ```
4. Verify that the code you wrote passes the style checks. You can do that with the following command (run from the root of the git repo)
    ```bash
    $ flake8
    ```
    If you do not have flake8 installed, you can install it with
    ```bash
    $ pip install -U flake8 
    ```
5. Once you are satisfied with your changes, you should make sure to commit them to your branch:
    ```bash
    # stage your changes
    $ git add bootcamp_module09/core/student_${xx}.py bootcamp_module09/core/tests/test_student_${xx}.py
    # commit with an informative message
    $ git commit -m "ENH make count_substring case insensitive"
    ```
   
### Adding a new feature to the repository

*If you get to this step with fewer than 20 minutes left in the activity, go ahead and skip to the "**Opening a Pull Request**" section*

In this section you will add a new feature to the repository.

You should create a file called `bootcamp_module09/contrib/student_${xx}` where you can implement your new feature.

Once you have done this, you can repeat the steps above in the **Modifying the behavior of an existing feature 
in the repository**, except with a twist: you get to decide what your function does.

A few guidelines that will help us moderate the activity:
* Please do not import any modules that are not a part of the base python installation (e.g., no `numpy` etc.)
* Please keep your new feature to fewer than 10 lines of code.
* Make sure you run the test suite and style checks locally _before_ advancing to "**Opening a Pull Request**"
    
    
### Opening a Pull Request
After you have made all of the changes you have made (and committed them with `git commit`, you should push them to GitHub
```bash
$ git push
```
If it is the first time you have pushed on a new branch, you will have to run
```bash
$ git push --set-upstream origin $BRANCHNAME
```

(Note: origin tells git that it should push to your GitHub repo)

You can then navigate to `https://github.com/gwarmstrong/bisb-bootcamp-2021-module09/`.

If you have pushed recently, you may notice a yellow/box that tells you that you can open a pull request.

Otherwise, you can 
1. Navigate to the  `Pull Requests` tab
2. Click `New pull request` in green on the right-hand side of the page
3. Click `compare across forks`
4. Change the base repository to your repository
4. Change the 'compare' branch to your new feature branch

Then, provide a description of your PR (including your student number, for this activity) and click `Create pull request`.

After submitting, make sure the automatic checks (GitHub Actions) pass (may 
take a couple minutes). If they fail, make sure your code
changes are passing the test suite and style checking locally.

If you make any changes after opening a PR, you can always push more commits. The PR will automatically be updated
and the CI checks will automatically be restarted.

Once your CI checks pass, or if you are having issues, let the instructors know!

We will try to provide feedback on your pull requests, as available.
