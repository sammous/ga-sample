---
type: slides
---

# Introduction to Decision Trees

---

# What is a Decision Tree ?

Tree shaped diagram used to predict a target value by learning simple decision rules inferred from the data features.

<p align="center">
<img src="img_slide1.png" class="center" alt="slide1" width="40%">
</p>

---

# From a table to a decision tree

| Windy | Sunny | Hot   | Won Game |
|-------|-------|-------|----------|
| False | False | True  | False    |
| True  | True  | True  | False    |
| False | True  | False | True     |
| False | False | False | True     |

<p align="center">
<img src="img_slide2.png" class="center" alt="slide1" width="30%">
</p>

---

# From a table to a decision tree

| Windy | Sunny | Hot   | Won Game |
|-------|-------|-------|----------|
| False | False | True  | False    |
| True  | True  | True  | False    |
| False | True  | False | True     |
| False | False | False | True     |

<p align="center">
<img src="img_slide3.png" class="center" alt="slide1" width="60%">
</p>

---

# Gini Impurity

<p align="center">
<img src="img_slide4.png" class="center" alt="slide1" width="60%">
</p>

---

# Gini Impurity

<p align="center">
<img src="img_slide5.png" class="center" alt="slide1" width="60%">
</p>

---

# Giny Impurity

<p align="center">
<img src="img_slide6.png" class="center" alt="slide1" width="60%">
</p>

---

# What is the Giny Impurity of the Windy node ?

To calculate the Gini impurity of a node, we compute the weighted average of Gini impurities for the leaf nodes.

<p align="center">
<img src="img_slide6.png" class="center" alt="slide1" width="60%">
</p>
<p align="center">
<img src="img_slide7.png" class="center" alt="slide1" width="60%">
</p>

---

# Choosing the right seperating node

<p align="center">
<img src="img_slide8.png" class="center" alt="slide1" width="60%">
</p>

---

# Once we choose one, we do the same for the left/right children nodes

<p align="center">
<img src="img_slide9.png" class="center" alt="slide1" width="40%">
</p>

---

# But when do we stop ?

<p align="center">
<img src="img_slide10.png" class="center" alt="slide1" width="30%">
</p>

---

# But when do we stop ?

<p align="center">
<img src="img_slide11.png" class="center" alt="slide1" width="31%">
</p>

---

# What about numerical values ?

| Windy | Sunny | Hot   | Temp | Won Game |
|-------|-------|-------|------|----------|
| False | False | True  | 11   | False    |
| True  | True  | True  | 14   | False    |
| False | True  | False | 19   | True     |
| False | False | False | 25   | True     |

- Sort the values
- Compute the average temperature between games
- Compute the Gini impurity for each average temperatures

<p align="center">
<img src="img_slide12.png" class="center" alt="slide1" width="20%">
</p>

---

# What about categorical values ?

| Color | Won Game |
|-------|-------|
| red | False |
| blue  | True  |
| green | True  |
| blue | False |

- Calculate the Gini impurity for each one as well as for each possible combination except for the one with every color choice.

<p align="center">
<img src="img_slide13.png" class="center" alt="slide1" width="40%">
</p>

---

# Now, let's practice!
