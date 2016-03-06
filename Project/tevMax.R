#TevMax Initial estimates for LogLikelihood using Gen Alg:
start.time <- Sys.time()
#Rootsolve
library(rootSolve)
#Genetic Algorithm
library(genalg)
library(GA)
#Data:
#3, 33, 146, 227, 342, 351, 353, 444, 556, 571, 709, 759, 836,
#tVec <- c( 860, 968, 1056, 1726, 1846, 1872, 1986, 2311, 2366, 2608, 2676, 3098, 3278, 3288, 4434, 5034, 5049, 5085, 5089, 5089, 5097, 5324, 5389, 5565, 5623, 6080, 6380, 6477, 6740, 7192, 7447, 7644, 7837, 7843, 7922, 8738, 10089, 10237, 10258, 10491, 10625, 10982, 11175, 11411, 11442, 11811, 12559, 12559, 12791, 13121, 13486, 14708, 15251, 15261, 15277, 15806, 16185, 16229, 16358, 17168, 17458, 17758, 18287, 18568, 18728, 19556, 20567, 21012, 21308, 23063, 24127, 25910, 26770, 27753, 28460, 28493, 29361, 30085, 32408, 35338, 36799, 37642, 37654, 37915, 39715, 40580, 42015, 42045, 42188, 42296, 42296, 45406, 46653, 47596, 48296, 49171, 49416, 50145, 52042, 52489, 52875, 53321, 53443, 54433, 55381, 56463, 56485, 56560, 57042, 62551, 62651, 62661, 63732, 64103, 64893, 71043, 74364, 75409,76057, 81542, 82702, 84566, 88682)

#242.46, 248.76, 502.44, 526.56, 564.18, 1492.56, 2026.74, 2218.44,2230.2, 2389.44, 2408.58, 3004.56, 3480.78, 3539.76, 3545.58, 3646.2,3652.5, 3980.64, 3985.2, 3991.98, 
tVec <- c(4061.4, 4640.52, 5217.6, 5849.52,5849.64, 5997.84, 6925.98, 6969.84, 6973.44, 6973.74, 7634.367,7802.247, 7989.087, 8268.131, 8688.251, 8756.051, 9079.511, 9191.531,9196.811, 9831.072, 9832.992, 10735.332, 10737.432, 10741.632,10742.112, 10919.172, 10961.532, 10998.552, 11053.092, 11388.612,11388.912, 11540.952, 11652.312, 12144.072, 12224.412, 12542.472,12545.592, 12550.992, 12735.732, 12751.152, 12852.012, 13087.148,13088.768, 13710.428, 14270.656, 14775.076, 14781.856, 15027.676, 15509.964, 15939.624, 16935.16, 17010.28, 17470.3, 17502.46,17704.96, 18022.78, 18288.04, 18324.22, 18498.4, 18518.14, 18526.54,18566.8, 18569.74, 18578.44, 18585.52, 18649.54, 18649.9, 18734.74,18734.92, 19643.26, 19650.94, 19709.8, 19732.36, 19740.64, 20309.736,20379.396, 20673.276, 20680.176, 20939.436, 20943.216, 21254.992,21366.028, 21779.968, 22051.588, 22116.148, 22415.548, 22448.428,23406.388, 24404.168, 24404.228, 24517.568, 24984.548, 25495.748, 25771.748, 25956.908, 26280.848, 26599.268, 27377.228, 27381.428,27954.568, 27956.788, 29194.588, 29417.548, 29525.848, 29584.828,29604.928, 29687.248, 30049.408, 30050.008, 30059.008, 31304.668,31321.468, 32322.508, 32322.656, 32322.772, 32323.012, 32323.492, 32324.332, 32743.672, 32743.792, 32803.852, 32890.732, 32896.912,32897.092, 32995.192, 32998.492, 33340.732, 34452.052, 34460.452,34552.132, 35173.912, 36049.612, 36684.232, 36684.652, 37064.032,37082.032, 37144.132, 37152.952, 37656.532, 37932.352, 38280.532,38285.632, 38763.532, 39399.952, 39975.292, 40197.652, 40284.232,40286.992, 40289.812, 40291.372, 40291.792, 40292.992, 40294.432,40401.472, 40432.912, 40737.172, 40796.272, 41064.232, 41085.952,41154.712, 41417.092, 41421.652, 41752.672, 43474.972, 43522.492,43823.662, 43824.682, 43992.682, 44105.992, 45719.542, 45811.732,46258.072, 46323.322, 48223.942, 48644.002, 48889.282, 50236.822)

#Create random binary input( for Chromosome)
x=runif(64,0,10)
x <- c(as.numeric(x%%2!=0))
#x=c(1,1,1,1,1,1,0,0)
LNl_prev <- 0
tVec <- as.numeric(tVec)
n <- length(tVec)
tn <- tVec[n]
sumT <- sum(tVec)

a0 <- n
c0 <- 1
#Log Likelihood wiht a
LNLa <- function(a0,b0,c0)
{
  a <- a0
  b <- b0
  c <- c0
  sumln <- 0
  for(i in 1:n)
  {
    sumln = sumln + (-exp((b-tVec[i])/c))+(b-tVec[i])/c+log(a) - log(c-exp(-exp(b/c))*c)
  }
  
  lnla <- (-a)*exp(-exp((b-tn)/c))/(1-exp(-exp(b/c)))  + sumln
  return(lnla)
}

#MLE of Parameter w
MLE_a <- function(a0)
{
  a <- a0
  b <- b0
  c <- c0
  
  mle_a <- -(exp(-exp(((-tn + b)/c)))/(1 - exp(-exp((b/c))))) + (n/a)
  return(mle_a)  
}

#Log-likelihood- reduced
LNL <- function(b0,c0)
{
  #Convert Binary to decimal
  b <- b0
  c <- c0
  sumL <- 0
  for(i in 1:n)
  {
    sumL = sumL + exp((b-tn)/c) - exp((b-tVec[i])/c) + ((b-tVec[i])/c) + log(1-exp(-exp(b/c))) + log(n) - log(c-exp(-exp(b/c))*c)
  }
return(sumL)
}

#MLE of Parameter Mu
MLE_b <- function(b0)
{
  
  b <- b0
  c <- c0
  sumb <- 0
  for(i in 1:n)
  {
    sumb = sumb + (1/c) + (exp((b-tn)/c)/c) - (exp((b-tVec[i])/c)/c) + exp(-exp(b/c)+(b/c))/((1-exp(-exp(b/c)))*c) - (exp(-exp(b/c)+(b/c)))/(c-exp(-exp(b/c))*c)
  }
  
  mle_b <- sumb
  return(mle_b)
}

#MLE of Parameter Theta
MLE_c <- function(c0)
{
  b <- b0
  c <- c0
  sumc <- 0
  for(i in 1:n)
  {
    sumc = sumc + -((exp(-exp((b/c)) + b/c)*b)/((1 - exp(-exp((b/c))))*(c^2))) - (exp((-tn + b)/c)*(-tn + b))/(c^2) - (1 - exp(-exp((b/c))) - (
      exp(-exp((b/c)) + (b/c))* b)/c)/(c - exp(-exp((b/c)))*c) - (b - tVec[i])/(c^2) + (exp((b - tVec[i])/c)*(b - tVec[i]))/(c^2)
  }
  
  mle_c <-  sumc
  return(mle_c)
}


#Function to convert fom binary to decimal
convertToDecimal <- function(x){
  sumnum <- 0
  sumdeci <- 0
  nn=length(x)
  xn<-x[1:12]
  dc<-x[13:32]
  for(i in 1:12)
    {
      sumnum=sumnum+xn[13-i]*2^(i-1)
    }
  for(i in 1:20)
  {
    sumdeci=sumdeci+dc[i]*2^(i-1)
  }
  
  returnVal <- as.numeric(paste(toString(sumnum),'.',toString(sumdeci),sep=''))
  #print(returnVal)
  return(returnVal)
}

#Eval Function for GA
GAfunc <- function(x){
  #print("X:")
  #print(x)
  b<-convertToDecimal(x[1:32])
  c<-convertToDecimal(x[33:64])
  
  "if(n1>n2)
  {
    c<-n1
    b<-n2
  }
  else
  {
    b<-n1
    c<-n2
  }"
  #print(b)
  #print(c)
  
  if(c<1000 || b<10)
    LNLnext <- LNL(n/sumT,5000)
  
  else
    LNLnext <- LNL(b,c)
  #print("LNL:")
  #print(LNLnext)
  #if(LNLnext - LNl_prev <0.001)
  if(LNLnext<-1300)
  {
    returnval <- 0
  }
  else{
    returnval <- LNLnext
  }
  LNl_prev = LNLnext
  return(returnval)
}

GAInvfunc <- function(x){
  print("X:")
  print(x)
  n1<-convertToDecimal(x[1:32])
  n2<-convertToDecimal(x[33:64])
  
  if(n1>n2)
  {
  c<-n1
  b<-n2
  }
  else
  {
  b<-n1
  c<-n2
  }
  print(b)
  print(c)
  
  
  #LNLnext <- LNL(n/sumT,1000)
  
  
  LNLnext <- LNL(c,b)
  print("LNL:")
  print(LNLnext)
  #if(LNLnext - LNl_prev <0.001)
  
  return(LNLnext)
}

#Gen Alg
GAmodel <- rbga.bin(size = 64, popSize = 50, iters = 100, mutationChance = 0.01, 
                    elitism = T, evalFunc = GAfunc)


summary(GAmodel, echo=TRUE)
bestSolution<-GAmodel$population[which.min(GAmodel$evaluations),]
print(GAInvfunc(bestSolution))




#b0 <-128
#c0<- 4095.998

#c0 <- 1152.172
#b0<- 2304.512

#SS3 Dataset
#b0 <- 0.532    #516.205
#c0 <- 512.1311 #2096.211
b0 <- 9.27   #256.64
c0 <- 128.16 #2048.15

#SYS1 Dataset
c0 <-100
b0<-0.2

prev_lllist <-0
curr_lllist <-1
#arule <- a0
brule <- b0
crule <- c0
llerror <- 0
llerror <- 1.0
j <- 1

while(llerror >1e-15)
{
  
  prev_lllist <- LNL(brule,crule)
  #arule <- stats::uniroot(MLE_a,c(1,130),maxiter=1e10,tol=1e-10,extendInt ="yes")$root
  brule <- stats::uniroot(MLE_b,c(1,40),maxiter=1e8,tol=1e-10,extendInt = "yes")$root
  crule <- stats::uniroot(MLE_c,c(1,40),maxiter=1e8,tol=1e-10,extendInt = "yes")$root
  curr_lllist <- LNL(brule,crule)
  llerror <- abs(curr_lllist - prev_lllist)
  
}
#Updated a value
aHat <- n/(exp(-exp(((-tn + brule)/crule)))/(1 - exp(-exp((brule/crule)))))


end.time <- Sys.time()
time.taken <- end.time - start.time
time.taken