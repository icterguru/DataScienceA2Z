clear all;
close all;
clc;
readData = csvread('titanic_data.csv', 1, 0);
gender = readData(:, 3);
histogram(gender);
xlabel("Female (0)            ------          Male (1)");
ylabel("Number of Survivors ");
grid on;
hold on;