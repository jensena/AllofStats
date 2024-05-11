p <- 0.3
n <- 1000

flips <- sample(c(0,1), n, replace = TRUE, prob = c(0.7, 0.3))

sum(flips)