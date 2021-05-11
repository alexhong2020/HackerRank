import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'miniMaxSum' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static void miniMaxSum(List<Integer> arr) {
    // Write your code here
        
        int min = 1000000000;
        int max = 1;
        long totsum = 0;
        long minsum = 0;
        long maxsum = 0;
        
        
        for(int k = 0; k < arr.size(); k++){
            if (arr.get(k) < min){
                min = arr.get(k);
            }
            if (arr.get(k) > max){
                max = arr.get(k);
            }

            totsum += arr.get(k);
        }
         
        //Tester
        //System.out.println(min + " " + max);
        
        
        minsum = totsum - max;
        maxsum = totsum - min;
            
        System.out.println(minsum + " " + maxsum);
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        Result.miniMaxSum(arr);

        bufferedReader.close();
    }
}

