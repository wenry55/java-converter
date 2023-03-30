public class SampleJavaProgram {

    public static void main(String[] args) {
        int oldVar1 = 10;
        int oldVar2 = 20;
        int add = 3;
        int sum = add(oldVar1, oldVar2);
        System.out.println("The sum of oldVar1 and oldVar2 is: " + sum);
    }

    public static int add(int a, int b) {
        int result = a + b;
        return result;
    }
}

