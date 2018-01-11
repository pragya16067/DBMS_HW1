import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.util.Random;

public class RandomFileGen {
	
	protected static String getRandomString() {
        String SALTCHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
        StringBuilder salt = new StringBuilder();
        Random rnd = new Random();
        while (salt.length() < 18) { // length of the random string.
            int index = (int) (rnd.nextFloat() * SALTCHARS.length());
            salt.append(SALTCHARS.charAt(index));
        }
        String saltStr = salt.toString();
        return saltStr;

    }
	
	public static void create() throws FileNotFoundException, UnsupportedEncodingException {
		Random rand = new Random();
		PrintWriter w = new PrintWriter("./src/TestInput.txt", "UTF-8");
		for (int i = 1; i <= 999; i++) {
		    try {
				
				w.print(rand.nextInt(100000)+"\t");
				w.print(getRandomString()+"\t");
				w.println(rand.nextInt(100));
					
				
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		w.close();
	}

	public static void main(String[] args) throws FileNotFoundException, UnsupportedEncodingException {
		create();

	}

}
