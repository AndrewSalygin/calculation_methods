// Интерполяционный многочлен в форме Ньютона
public class Main {
    public static double[][] dividedDifferences(double[] x, double[] y) {
        int n = x.length;
        double[][] f = new double[n][n];

        // инициализируем массив
        for (int i = 0; i < n; i++) {
            f[i] = new double[n - i];
        }

        // заполняем первый столбец
        for (int i = 0; i < x.length; i++) {
            f[i][0] = y[i];
        }
        // i - столбец, j - строка
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < n - i; j++) {
                // берём всегда предыдущий столбец
                // 0 и 1, 1 и 2 строку и т.д
                // в иксах 1 0, 2 1, ..., 2 0, 3 1 и т. д.
                f[j][i] = (f[j + 1][i - 1] - f[j][i - 1]) / (x[i + j] - x[j]);
            }
        }

        return f;
    }
    public static double interpolate(double[] x, double[] y, double[][] dividedDiffs, double value) {
        int n = x.length;
        double result = 0;

        for (int i = 0; i < n; i++) {
            double term = dividedDiffs[0][i];
            for (int j = 0; j < i; j++) {
                term *= (value - x[j]);
            }
            result += term;
        }

        return result;
    }

    public static void main(String[] args) {
        // Задайте значения точек и x-координату, для которой нужно интерполировать
        double[] x = {-2.0, -1.0, 0.0, 2.0};
        double[] y = {-8.0, -1.0, 0.0, 8.0};

        double[][] dividedDiffs = dividedDifferences(x, y);

        // выводим разделённые разницы
        System.out.println("Разделённые разницы:");
        for (int i = 0; i < dividedDiffs.length; i++) {
            for (int j = 0; j < dividedDiffs.length - i; j++) {
                System.out.print(dividedDiffs[i][j] + " ");
            }
            System.out.println();
        }

        System.out.println();
        System.out.println("x\t\tf(x)");
        for (int i = 1; i <= x.length; i++) {
            System.out.println(x[i - 1] + "    " + y[i - 1]);
        }

        System.out.println();
        System.out.println("x\t\tf(x)");
        for (int i = 1; i <= x.length; i++) {
            System.out.println(x[i - 1] + "    " + y[i - 1]);
            if (i != x.length) {
                double interpolatedValue = interpolate(x, y, dividedDiffs, (x[i - 1] + x[i]) / 2);
                System.out.println((x[i - 1] + x[i]) / 2 + "    " + interpolatedValue);
            }
        }
    }
}
