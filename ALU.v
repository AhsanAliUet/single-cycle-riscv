`timescale 1ns/1ps
module ALU(ALUout, ALUin1, ALUin2, control, zFlag);

	input [2:0] control;
	input [31:0] ALUin1, ALUin2;
	output reg [31:0] ALUout;
	output reg zFlag;
	
	
	always @ (*)
	begin
		zFlag = (ALUin1 == ALUin2);
		case (control)
			3'b000: begin
					ALUout <= ALUin1 + ALUin2;    //add
			end
			3'b001: begin                          //for subtraction
					ALUout <= ALUin1 - ALUin2;

			end			
			3'b010: begin
			       ALUout <= ALUin1 & ALUin2;     //and
			end
			3'b011: begin
					ALUout <= ALUin1 | ALUin2;     //or
			end
			3'b101: begin //SLT instruction, checking whether ALUin1 in > or not
						
					if((ALUin1 - ALUin2) >= 32'h80000000) ALUout <= 32'b1; 			                //slt
					else ALUout <= 32'b0;                 //Implementing signed number comparison
			end
			
			3'b100: begin

					if ((ALUin1 - ALUin2) >= 32'b0) ALUout <= 32'b0;
					else ALUout <= 32'b1;
			end
			
			3'b110: begin
					ALUout <= ALUin1 ^ ALUin2;           //XOR
			end 


			
			default: begin ALUout <= ALUin1 + ALUin2; end
			
		endcase
	end
endmodule