<div class="span-sm-11 hr_tour-problem-statement problem-statement"><div class="content-text challenge-text mlB">
<div class="challenge_problem_statement"><div class="msB challenge_problem_statement_body"><div class="hackdown-content"><p>Alright !!</p>

<p>Now Naruto is in complete control of <strong>the nine-tailed fox</strong>. Shikamaru, the most intelligent ninja on the team, made a plan. He said that all the ninjas should divide themselves into groups of two members and attack Orochimaru and his army from all directions. Such that they won't have any place to run or hide.</p>

<p><img src="https://s3.amazonaws.com/hr-assets/0/1642514956-104528bd01-naruto-and-his-friends-naruto-37735959-599-424.jpg" alt="image" title=""></p>

<p>Assume each ninja is represented as a bracket sequence.</p>

<p>A bracket sequence is a string containing only characters "(" and ")".</p>

<p>A regular bracket sequence is a bracket sequence that can be transformed into a correct arithmetic expression by inserting characters "1" and "+" between the original characters of the sequence. For example, bracket sequences "()()", "(())" are regular (the resulting expressions are: "(1)+(1)", "((1+1)+1)"), and ")(" and "(" are not.</p>

<p>You are given n ninjas (means n bracket sequences) s1,s2,…,sn. Calculate the number of pairs i,j(1≤i,j≤n) such that the bracket sequence si+sj is a regular bracket sequence. Operation + means concatenation i.e. "()(" + ")()" = "()()()". Since in ninja village it is considered a good sign if group's bracket sequence is regular.</p>

<p>If si+sj and sj+si are regular bracket sequences and i≠j, then both pairs (i,j) and (j,i) must be counted in the answer. Also, if si+si is a regular bracket sequence, the pair (i,i) must be counted in the solution.</p>

<p>You must inform the total number of such teams possible.</p></div></div></div><div class="challenge_input_format"><div class="msB challenge_input_format_title"><p><strong>Input Format</strong></p></div><div class="msB challenge_input_format_body"><div class="hackdown-content"><p>The first line contains one integer <strong>n</strong> — the number of bracket sequences. The following n lines contain bracket sequences — non-empty strings consisting only of characters "(" and ")".</p></div></div></div><div class="challenge_constraints"><div class="msB challenge_constraints_title"><p><strong>Constraints</strong></p></div><div class="msB challenge_constraints_body"><div class="hackdown-content"><ul>
<li>1 ≤ n ≤ 3⋅10^5</li>
<li>length of each string &lt;= 10</li>
</ul></div></div></div><div class="challenge_output_format"><div class="msB challenge_output_format_title"><p><strong>Output Format</strong></p></div><div class="msB challenge_output_format_body"><div class="hackdown-content"><p>In the single line print a single integer — the number of pairs i,j(1≤i,j≤n) such that the bracket sequence si+sj is a regular bracket sequence.</p></div></div></div><div class="challenge_sample_input"><div class="msB challenge_sample_input_title"><p><strong>Sample Input 0</strong></p></div><div class="msB challenge_sample_input_body"><div class="hackdown-content"><div class="highlight"><pre><span></span><span class="err">3</span>
<span class="err">)</span>
<span class="err">()</span>
<span class="err">(</span>
</pre></div>
</div></div></div><div class="challenge_sample_output"><div class="msB challenge_sample_output_title"><p><strong>Sample Output 0</strong></p></div><div class="msB challenge_sample_output_body"><div class="hackdown-content"><div class="highlight"><pre><span class="err">2</span>
</pre></div>
</div></div></div><div class="challenge_explanation"><div class="msB challenge_explanation_title"><p><strong>Explanation 0</strong></p></div><div class="msB challenge_explanation_body"><div class="hackdown-content"><p>suitable pairs are (3,1) and (2,2).</p></div></div></div><div class="challenge_sample_input"><div class="msB challenge_sample_input_title"><p><strong>Sample Input 1</strong></p></div><div class="msB challenge_sample_input_body"><div class="hackdown-content"><div class="highlight"><pre><span></span><span class="err">2</span>
<span class="err">()</span>
<span class="err">()</span>
</pre></div>
</div></div></div><div class="challenge_sample_output"><div class="msB challenge_sample_output_title"><p><strong>Sample Output 1</strong></p></div><div class="msB challenge_sample_output_body"><div class="hackdown-content"><div class="highlight"><pre><span class="err">4</span>
</pre></div>
</div></div></div><div class="challenge_explanation"><div class="msB challenge_explanation_title"><p><strong>Explanation 1</strong></p></div><div class="msB challenge_explanation_body"><div class="hackdown-content"><p>any pair is suitable, namely (1,1),(1,2),(2,1),(2,2).</p></div></div></div>
            </div>
        </div>
