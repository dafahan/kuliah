import java.util.Scanner;

public class no2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Membaca jumlah input
        int n = input.nextInt();
        input.nextLine(); // Membaca karakter newline setelah input integer

        // Inisialisasi string untuk menyimpan hasil penggabungan
        StringBuilder result = new StringBuilder();

        // Membaca n string dan menggabungkannya
        for (int i = 0; i < n; i++) {
            String str = input.nextLine();
            result.append(str).append(" "); // Menggabungkan string dengan spasi
        }

        // Menghapus spasi ekstra di akhir
        String finalResult = result.toString().trim();

        // Mencetak hasil
        System.out.println(finalResult);

        input.close();
    }
}
