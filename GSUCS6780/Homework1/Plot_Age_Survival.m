clear all;
close all;
clc;
A = csvread('titanic_data.csv', 1, 0);
x = A(:, 1);
y = A(:, 2);

% plot(x, y, '*', 'linewidth', 2);
plot(x, y, '*');
xlabel("Not Survived (0) -- Survived (1)");
ylabel("Age (year)");
grid on;
% plot.show();
hold on;