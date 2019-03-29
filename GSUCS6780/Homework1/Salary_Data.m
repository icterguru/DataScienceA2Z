clear all;
close all;
clc;
A = csvread('Salary_Data.csv', 1, 0);
x = A(:, 1);
y = A(:, 2);
% plot(x, y, '*', 'linewidth', 2);
% plot(x, y, '*');
% hold on;

histogram(y);
xlabel("Experience (year)");
ylabel("Salary (x $1000)");
grid on;
% plot.show();
hold on;