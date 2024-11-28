library(readxl)

ChemicalDisease <- read_excel('ChemicalDiseaseEV.xlsx',sheet = 'Sheet1')
Chemical <- read_excel('ChemicalDiseaseEV.xlsx',sheet = 'Sheet2')
Disease <- read_excel('ChemicalDiseaseEV.xlsx',sheet = 'Sheet3')

df1 <- merge(ChemicalDisease,Chemical,by='ChemicalName')
df2<- merge(df1,Disease,by='DiseaseName')

rating <- df2[,c(5,6,4)]

write.table(rating,file = 'ratings.dat', sep = "\t", row.names = FALSE, quote = FALSE,col.names = FALSE)



# 新的Chemical-Disease添加ID
Chemical-Diseasenew <- read_excel('Chemical-Diseasenew.xlsx')
df1new <- merge(Chemical-Diseasenew,Chemical,by='ChemicalName',all=TRUE)
# 提取没有ID的化合物重新定义ID


df2<- merge(df1,Disease,by='DiseaseName')