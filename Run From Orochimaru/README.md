<div class="span-sm-11 hr_tour-problem-statement problem-statement">
<div class="content-text challenge-text mlB">
<div class="challenge_problem_statement"><div class="msB challenge_problem_statement_body"><div class="hackdown-content"><p>You got the password, but Orochimaru and his army started to chase you by the time you got it. You and Kakashi are heavily outnumbered, so you decided to run for now.</p>

<p>Kakashi remembered a secret maze of the hidden leaf village that can take you out of the village in no time, and since none except for the leaf village ninjas knows how to solve it. It is a perfect place for you to run, but Kakashi is too weak to solve that maze because of his recent battle against Kabuto. So he explained to you the logic of the maze.</p>

<p><img src="https://s3.amazonaws.com/hr-assets/0/1642473674-16bbef15ec-kakashi-hatake-run.gif" alt="image" title=""></p>

<p>Maze is developed by keeping the Chakara system of a ninja in mind (Chakara can be thought of as the inner energy of a ninja). Maze is an N × M grid where each cell has a <strong>Chakara Reduction Cost</strong> associated with it. Find the minimum reduction cost to reach the last cell (N-1, M-1) of the gird from its first cell (0, 0). We can only move one unit right or one unit down from any cell, i.e., from the cell (i, j); we can move to (i, j+1) or (i+1, j). After each move, your Chakara reduces by the amount of the cell's Chakara Reduction Cost. So if you don't choose the best path, you will be dead the moment you leave the maze as you won't have any Chakara left.</p></div></div></div><div class="challenge_input_format"><div class="msB challenge_input_format_title"><p><strong>Input Format</strong></p></div><div class="msB challenge_input_format_body"><div class="hackdown-content"><ul>
<li>T (number of test cases)</li>
<li>for each case, Two integers, N and M (size of Maze)</li>
<li>N x M integers, Chakara Reduction Cost</li>
</ul></div></div></div><div class="challenge_constraints"><div class="msB challenge_constraints_title"><p><strong>Constraints</strong></p></div><div class="msB challenge_constraints_body"><div class="hackdown-content"><ul>
<li>T &lt;= 100</li>
<li>N &lt;= 100</li>
<li>M &lt;= 100</li>
<li>cost[i][j] &lt;= 10^5</li>
</ul></div></div></div><div class="challenge_output_format"><div class="msB challenge_output_format_title"><p><strong>Output Format</strong></p></div><div class="msB challenge_output_format_body"><div class="hackdown-content"><ul>
<li>T lines containing minimum possible chakara reduction cost.</li>
</ul></div></div></div><div class="challenge_sample_input"><div class="msB challenge_sample_input_title"><p><strong>Sample Input 0</strong></p></div><div class="msB challenge_sample_input_body"><div class="hackdown-content"><div class="highlight"><pre><span></span><span class="err">1</span>
<span class="err">5 5</span>
<span class="err">4 7 8 6 4</span>
<span class="err">6 7 3 9 2</span>
<span class="err">3 8 1 2 4</span>
<span class="err">7 1 7 3 7</span>
<span class="err">2 9 8 9 3 </span>
</pre></div>
</div></div></div><div class="challenge_sample_output"><div class="msB challenge_sample_output_title"><p><strong>Sample Output 0</strong></p></div><div class="msB challenge_sample_output_body"><div class="hackdown-content"><div class="highlight"><pre><span></span><span class="err">36</span>
</pre></div>
</div></div></div><div class="challenge_explanation"><div class="msB challenge_explanation_title"><p><strong>Explanation 0</strong></p></div><div class="msB challenge_explanation_body"><div class="hackdown-content"><p><img src="https://s3.amazonaws.com/hr-assets/0/1642436851-4eecebe7d3-Min-Cost-Path-in-a-Matrix.png" alt="image" title=""></p></div></div></div>
            </div></div>
