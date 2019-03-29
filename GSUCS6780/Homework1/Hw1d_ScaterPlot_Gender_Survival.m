clear all;
close all;
clc;

readData = csvread('titanic_data.csv', 1, 0);
gender = readData(:, 3);
survival = readData(:, 1);

% plot(gender, survival, '*', 'linewidth', 2);
plot(gender, survival, '*');
xlabel("Gender (Male) -- Female ");
ylabel("Deccased (0) ------------- Survived (1)");

grid on;
hold on;