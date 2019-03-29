clear all;
close all;
clc;
readData = csvread('titanic_data.csv', 1, 0);
fare = readData(:, 7);
survival = readData(:, 1);
boxplot(fare, survival);
xlabel("Not Survived (0)     ---------        Survived (1)");
ylabel("Fare ($)");
grid on;
hold on;