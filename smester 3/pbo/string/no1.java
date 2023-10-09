import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class no1 {

    public static void main(String[] args) {
        Scanner i = new Scanner(System.in);
        String kata = i.nextLine();
        int x = i.nextInt();
        int y = i.nextInt();
        System.out.println(kata.substring(x,y));
    }
}