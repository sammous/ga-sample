---
title: 'Chapter 1: Introduction to Decision Trees'
description:
  'This chapter will introduce you to the basics of understanding what are decision trees and building them.'
prev: null
next: /chapter2
type: chapter
id: 1
---

<exercise id="1" title="Requirements">

This chapter requires the following concepts/basics :
- Introduction to machine learning
- Python coding skills
- Data manipulation with Pandas
- Basics with Scikit-learn

</exercise>

<exercise id="2" title="Lesson" type="slides">

<slides source="chapter1_01_introduction">
</slides>

</exercise>

<exercise id="3" title="Some coding practice">

In this exercise, you will build your first _Decision Tree_ classifier using the `scikit-learn` and `pandas` libraries.

To test your implementations, you can click on the **Run Code** button anytime. Once you want to test your implementation, you
can submit it by clicking on the **Submit** button.

<codeblock id="01_03">

Check the documentation of scikit-learn to build a DecisionTree classifier [here](https://scikit-learn.org/stable/modules/tree.html).

</codeblock>

</exercise>

<exercise id="4" title="Wrapping up">
Let's ask some questions about the slides before wrapping up.

What is the Gini index of the *Hot* node ?

<img src="gini.jpg" class="center" alt="giniex" width="80%">

<choice>

<opt text="0.28" correct="true">

Good job!

</opt>

<opt text="0.52">

Don't forget to calculate the weighted average of both Gini impurity of the leaf nodes.

</opt>

</choice>

</exercise>

<exercise id="5" title="Next lesson">

Now that we have seen the basics of a decision tree, even though it is simple to compute, it comes with some disadvantages :

- It is easily prone to overfitting
- If the data has a high variance, then the model can get unstable
- Complicated decision trees tend to get a low bias, which makes it harder to work with new data

</exercise>