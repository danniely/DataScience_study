# Used Car Price Tendency Prediction

In this module, we are going to make prediction towards used cars' price tendency. There are total 2 parts in this project.\
In part 1, we will determine the price drop tendency catergorized by each car brand.\
In part 2, we will predict the actual price drop of the most popular model of each car brand.


## Part 1
* [Price drop prediction by brands](https://github.com/danniely/Used-Car-Price/blob/Hyunho/Used_Car_price.ipynb)

In part 1, the main goal is to determine the price drop tendency with respect to the car's mileage and its manufactured year. Before calculating the exact price of each car, I think it was better to show the general price drop trend, so it allows the user to get a rough idea of their car price variation.\
\
Since part 1 does not handle the exact price amount, it shows the remaining price percentage according to the price gradient. Each gradient is collected with each car brand, regardless of its model. In other words, it is to determine the companies' market value and how they were reflected in the car industry. Thus people could consider the brand name before purchase so that they could profit more when they resell.\
\
My first instinct about the price variation was 'luxury car will show a greater price drop due to higher insurance rate, MPG and etc. We will figure that out through part 1 if my hypothesis was actually correct.

![part_1_result](https://user-images.githubusercontent.com/37637823/56077712-3a874f80-5d94-11e9-8727-c8a4d43fc4fe.png)

## Part 2
* [Price drop prediction by car models](https://github.com/danniely/Used-Car-Price/blob/Hyunho/Car_model_price_prediction.ipynb)

In part 2, I am going to present more precise information about car price. Unlike previous part 1, lists of cars will be categorized by each brand, and furthermore, their model. After categorizing data by each model, it allows performing the actual price estimation, since they all have the same attributes except its mileage and manufactured year. Then, the user could find the estimated price of a used car with their own unique mileage and manufactured year. 
![3dScatter](https://user-images.githubusercontent.com/37637823/62366193-33fa2f00-b561-11e9-902c-ba4fbd9afff3.jpg)
\
The 3d scatter plot above was from the dataset. This sample indicates that the mileage, manufactured year and the price of a car are related in some way. The lighter the mark is, more behind it exists. It is possible to observe the price of a car tends to get cheaper with higher mileage and longer driven period. Therefore, multivariate linear regression has been applied to estimate a used car price with user's own mileage and manufactured year.
![2](https://user-images.githubusercontent.com/37637823/62366300-7a4f8e00-b561-11e9-9170-1a811e04f60d.jpg)

