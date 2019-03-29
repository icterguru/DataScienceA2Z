clear all;
close all;
clc;
readData = csvread('titanic_data.csv', 1, 0);
gender = readData(:, 3);
survival = readData(:, 1);

histogram(gender);
xlabel("Not Survived (0)     ---------        Survived (1)");
ylabel("Number of People");
grid on;
hold on;