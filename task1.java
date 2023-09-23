import java.util.*;
import java.lang.*;
import java.text.DecimalFormat;

public class Main
{
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
        
        System.out.println("x    |  Sn   |    n");
        for (int xStart = -20; xStart <= 20; xStart+=1) {
            int x = xStart;
            double eps = 0.001;
            int denominator = 1;
            double nextValue = x;
            double sn = 0;
            int n = 0;
            int i = 2;
            
            while (Math.abs(nextValue) > eps) {
                n++;
                sn += nextValue;
                nextValue *= (double)((-1) * x * x) / (i * (i + 1));
                i +=2;
            }
            String formattedDouble = new DecimalFormat("#0.00").format(sn);
            System.out.println(xStart + " | " + formattedDouble + " | " + (n + 1));
        }
        
	}
}
