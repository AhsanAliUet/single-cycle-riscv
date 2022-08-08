
# Single Cycle RISC-V Processor

It is a repository on which single cycle RISC-V processor is made supporting R, I, S, B and J type instructions.

Also, the simulations are also given with pictures of waveforms in the file Simulations of Single Cycle RISC.pdf file. 

I have some silly comments in Verilog files, ignore them because "Code never lies, comments sometimes do :)"

However, according to my time span, I was able to write some of the code and some changes are left and I recommend some to change my code so that we can bring this code to next level that everyone can understand the single cycle risc-v processor.

I have checked all of the instructions I supported for this but I want to check on your end also.


## How to use this project?

I am giving the instructions (instruction memory of program memory) to the processor from a file called machineCodeInBinary.txt which is generated using Python script which uses assembly instructions file called assemFile.txt

We can write our assembly instructions in assemFile.txt and then save the file. After that, there is a file mainFile.py in the folder Complete_Assembler, we can run this file using any Python Interpreter (I use Anaconda). 

Python Interpreter will read assemFile.txt and convert this to machineCodeInBinary.txt which contains binary code to insert in the Instruction memory of processor. 
Now we are ready to run/boot our processor. 


## Putting it all together

Finally, to run all Verilog files in QuestaSim (I prefer this), add all Verilog (.v) file in the new project of QuestaSim, then simulate the file tb_RISC.v

See all the waveform according to your will, enjoy and debug it :)


## Author

- [@Ahsan Ali](https://github.com/AhsanAliUet)

