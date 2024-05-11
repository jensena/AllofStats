# Flip a coin 1000 times with probability of success (heads) p = 0.3

p <- 0.3
n <- 1000

flips <- sample(c(0, 1), n, replace = TRUE, prob = c(1 - p, p))

sum(flips)