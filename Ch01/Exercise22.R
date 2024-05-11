# Flip a coin with probability of success (heads) p = 0.3
# Use sample sizes 10, 100, 1000

p <- 0.3
ns <- c(10, 100, 1000)

mapply(function(sizes) sum(sample(x=0:1, size=sizes, replace=TRUE, prob=c(1-p,p))), ns)