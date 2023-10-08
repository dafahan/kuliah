import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;

import java.io.FileReader;
import java.io.Reader;
import java.util.ArrayList;
import java.util.List;

public class App {
    public static void main(String[] args) throws Exception {
        String[][][] dataMahasiswa = new String[10][3][3]; 
       

        try (Reader reader = new FileReader("src/DataMahasiswa.csv")) {
            CSVParser csvParser = new CSVParser(reader, CSVFormat.DEFAULT.withHeader());

            
            List<CSVRecord> records = csvParser.getRecords();
            for (int i = 0; i < records.size(); i++) {
                CSVRecord record = records.get(i);
                dataMahasiswa[i][0][0] = record.get("Nama");
                dataMahasiswa[i][1][1] = record.get("Kelas");
                dataMahasiswa[i][2][2] = record.get("Npm");
            }
        }

        
        for (int i = 0; i < dataMahasiswa.length; i++) {
            System.out.println("dataMahasiswa[" + i + "][0][0] = " + dataMahasiswa[i][0][0]);
            System.out.println("dataMahasiswa[" + i + "][1][1] = " + dataMahasiswa[i][1][1]);
            System.out.println("dataMahasiswa[" + i + "][2][1] = " + dataMahasiswa[i][2][2]);
        }
    }
}

/*
 * to run 
javac -d bin -cp .;lib/commons-csv-1.10.0.jar src/App.java
java -cp bin;lib/commons-csv-1.10.0.jar App
*/
 