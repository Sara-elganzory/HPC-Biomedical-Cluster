# Import PySpark and ML libraries
from pyspark.sql import SparkSession
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.feature import VectorAssembler

# Initialize the Spark Session
spark = SparkSession.builder.appName("BioinformaticsML").getOrCreate()

# Load the dataset and assemble features into a vector
df = spark.read.csv("breast_cancer_data.csv", header=True, inferSchema=True)
feature_cols = df.columns[:-1]
assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
data = assembler.transform(df)

# Split the data into training and test sets
train_data, test_data = data.randomSplit([0.8, 0.2])

# Initialize and train the RandomForest model
rf = RandomForestClassifier(labelCol=df.columns[-1], featuresCol="features", numTrees=100)
model = rf.fit(train_data)

# Make predictions on test data and calculate accuracy
predictions = model.transform(test_data)
accuracy = predictions.filter(predictions[df.columns[-1]] == predictions.prediction).count() / test_data.count()

# Display results and stop the Spark session
print(f"Accuracy on test data: {accuracy:.4f}")
spark.stop()
