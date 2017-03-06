package clientHandlers;

import org.json.simple.parser.JSONParser;
import org.json.simple.JSONObject;
import org.json.simple.parser.ParseException;

public class JSONExtractor implements MessageExtractorInterface{
    @Override
    public PeripheralAction handleMessage(String input){
        JSONParser parser = new JSONParser();
        String action = "";
        long id = -1;
        try {
            // Convert input string to JSON object, look for action description
            Object inObj = parser.parse(input);
            JSONObject message = (JSONObject) inObj;
            JSONObject actionDescription = (JSONObject) message.get("action");
            if(actionDescription == null){

                return new PeripheralAction("NOP",-1);
            }

            // Parse action type and peripheral id
            action = (String) actionDescription.get("type");
            id = (long) actionDescription.get("id");
        }catch(ParseException pe){
            // If the message we received cannot be parsed or does not contain the required fields, we return
            // no-operation. The clientHandlerThread will take special action upon encountering this object.
            return new PeripheralAction("NOP",-1);
        }
        // Return a new messageObject containing an id and an actionString
        return new PeripheralAction(action,id);
    }

}