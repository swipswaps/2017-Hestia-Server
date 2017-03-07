package peripherals;
import java.io.IOException;

public interface IPeripheral {
	public void performAction(String action) throws ActionNotDefinedException, IOException, InterruptedException;
}