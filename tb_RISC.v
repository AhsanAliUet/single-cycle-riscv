`timescale 1ns/1ps
module tb_RISC();
	reg clk, rst;
	
	initial begin
		clk = 0;
	end
	
	always #5 clk = ~clk;
	
	RISC my_RISC(clk, rst);
	
	initial begin
		rst = 1;
		#2; rst = 0;
	end

endmodule