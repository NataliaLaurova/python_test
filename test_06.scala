import scala.io.Source
import java.io.{File, PrintWriter}

object test_06 {
	def main(args: Array[String]) {

		print("The question number 6 in Scala.\n")

		// Read Text
		val text = Source.fromFile("test.txt").mkString

		// Print from Text
		println("Scala: " + text)
		
		// Write to CSV
		val writer = new PrintWriter(new File("scala.csv"))
		var csvData = new StringBuffer("")
		csvData.append(text)
            	writer.write(csvData.toString())
		writer.close()
		
		println("CSV created\n")	
	}
}
