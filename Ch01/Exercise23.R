A <- c(2, 4, 6)
B <- 1:4
n <- 100000

draws <- sample(1:6, n, replace=TRUE)

PA <- sum(draws %in% A)/n
PB <- sum(draws %in% B)/n
PAB <- sum(draws %in% intersect(A, B))/n

PA*PB
PAB