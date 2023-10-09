import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class no3 {

    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);
        String kata = inp.nextLine();
        String kata2 = inp.nextLine();
        int tested = kata.indexOf(kata2);
        if(tested==-1){
            System.out.println("Tidak");
        }else{
            System.out.println("Ya");
 }
}
}