This is a little study about the [non-atomicity of Long operations in Java 32-bit](http://docs.oracle.com/javase/specs/jls/se7/html/jls-17.html#jls-17.7).

## Building ##

You must have [Docker](https://www.docker.com/community-edition) installed¹.
Our runtime will be the [cortinico/java8-32bit](https://hub.docker.com/r/cortinico/java8-32bit/) Docker image.

To compile the `.java` files, run
```
./bin/build
```
The compiled `.class` files will be at `tmp` directory.

#### Running ####

You can run the experiment with
```
./bin/run <repetitions>
```
This will run a container that executes the script at `scripts/perform.sh`, passing `<repetitions>` as its parameter.

Example: running 10 repetitions
```
$ ./bin/run 10
1111111111111111111111111111111100000000000000000000000001100100
0000000000000000000000000000000011111111111111111111111110011100
1111111111111111111111111111111100000000000000000000000000000000
0000000000000000000000000000000011111111111111111111111110011100
0000000000000000000000000000000011111111111111111111111110011100
0000000000000000000000000000000011111111111111111111111110011100
0000000000000000000000000000000011111111111111111111111110011100
0000000000000000000000000000000011111111111111111111111110011100
```

Note that are less than 10 results, as the result is only reported when the bug occurs within 1 second. (What `perform.sh` does is `timeout 1 java -d32 -cp tmp Principal`)
You can then redirect `./bin/run` to a file and use `experiment_parser.py` to analyze the results:
```
$ ./bin/run 100 > experiments.log
$ python experiment_parser.py experiments.log
Read 46 values, 6 unique:
1111111111111111111111111111111100000000000000000000000000000000
0000000000000000000000000000000011111111111111111111111110011100
1111111111111111111111111111111100000000000000000000000001100010
1111111111111111111111111111111100000000000000000000000001100100
0000000000000000000000000000000011111111111111111111111111111010
0000000000000000000000000000000011111111111111111111111111111101
```

---

Pull requests are welcome.

---
1 - I did not manage to get a 32-bit Java runtime to work with macOS. Any suggestions?
