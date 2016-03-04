cat join2_gen*.txt | ./join2_mapper.py |sort| ./join2_reducer.py |less

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -input /user/cloudera/input -mapper /home/cloudera/join2_mapper.py -reducer /home/cloudera/join2_reducer.py -numReduceTasks 1 -output /user/cloudera/output_join2

hdfs dfs -cat /user/cloudera/output_join2/part-00000| less

answer should consists of 20 entries with first 3:
Almost_Games    49237
Almost_News     46592
Almost_Show     50202
