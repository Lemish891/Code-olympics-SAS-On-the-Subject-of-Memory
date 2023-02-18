def pin_decoder(sequences):
    presses = [["",""],["",""],["",""],["",""],["",""]]

    stages = [
        {
        "1" : "1",
        "2" : "1",
        "3" : "2", 
        "4" : "3"
    },
    {
        "1" : "l 4",
        "2" : [0,0],
        "3" : "0", 
        "4" : [0,0]
    },
    {
        "1" : [1,1],
        "2" : [0,1],
        "3" : "2", 
        "4" : "l 4"
    },
    {
        "1" : [0,0],
        "2" : "0",
        "3" : [1,0], 
        "4" : [1,0]
    },
    {
        "1" : [0,0],
        "2" : [1,0],
        "3" : [2,0], 
        "4" : [3,0]
    }]
    
    output_pin = ""
    for i in range(len(sequences)):
        sequence = sequences[i]
        code = sequence[:3]
        prompt = sequence[4]
        stage = stages[i]
        instruction = stage[str(prompt)]
        if isinstance(instruction, list):
            instruction = presses[instruction[0]][instruction[1]]
        press = presses[i]
        if instruction.split(" ")[0] == "l":
            label = instruction.split(" ")[1]
            output_pin = output_pin + label
            presses[i][1] = "l " + label
        else:
            output_pin = output_pin + str(code[int(instruction)])
            presses[i][1] = "l " + str(code[int(instruction)])
        presses[i][0] = instruction
    print(output_pin)



sequence =  [[1,3,2,4,1],[3,1,2,4,3],[2,3,4,1,2],[2,1,4,3,1],[4,1,2,3,4]]
pin_decoder(sequence)