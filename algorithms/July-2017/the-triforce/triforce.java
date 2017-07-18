import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();

        StringBuilder str = new StringBuilder();
        int spaceSize = (2 * N) - 1;
        int starSize = 1, blank = 1;
        
        for(int i = 0; i < (2* N); i++) {
            for(int j = 0; j < spaceSize; j++) str.append(" ");
            for(int j = 0; j < starSize; j++)
                str.append(i >= N && (j >= blank && j < starSize - blank) ? " " : "*");
            str.append("\n");
            
            starSize += 2;
            spaceSize--;
            if(i >= N) blank += 2;
                
        }
        str.setCharAt(0, '.');

        System.out.print(str.toString());
    }
    