public class FindTheAverage {
  public void findAvg(int a, int b, int c) {
    int sum = a + b + c;
    int avg = sum / 3;
    System.out.println(avg);
  }

  public static void main(String[] args) {
    FindTheAverage obj = new FindTheAverage();
    obj.findAvg(10, 20, 30);
  }
}
