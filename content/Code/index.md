---
summary: Code examples
title: "Code Examples"
date: July 27, 2021
type: code
---

This is just to showcase two things currently:

I can link to scripts like the following (these are just some scripts for a larger NLP Project):

[Pulling Japanese Text](jp_regex.py) \
[Pulling Data from Reddit](reddit_data.py)

We can also naturally showcase R, Python, or any other language we are interested in:

```{r}
summary(Orange)
```

```{r echo=FALSE}
library(ggplot2)
oplot <- ggplot(Orange, aes(x = age, 
                   y = circumference, 
                   colour = Tree)) +
  geom_point() +
  geom_line() +
  guides(colour = FALSE) +
  theme_bw()
oplot
```

```{python}
for i in range(0,5):
print(i)
```
