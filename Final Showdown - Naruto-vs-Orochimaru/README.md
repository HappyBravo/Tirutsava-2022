<div class="span-sm-11 hr_tour-problem-statement problem-statement">
<div class="content-text challenge-text mlB">
<div class="challenge_problem_statement"><div class="msB challenge_problem_statement_body"><div class="hackdown-content"><p>Finally, the time has come. An intense battle between both parties has started. </p>

<p>Both Naruto and Orochimaru on the battlefield have come face-to-face and are ready to fight till death. Initially, the fight was in Naruto's favor. Still, suddenly, it turns out that Orochimaru has absorbed all of his armies and became the strongest ninja on earth (since he now possesses the strength of an entire army). </p>

<p><img src="https://s3.amazonaws.com/hr-assets/0/1642517748-058ee18c9d-WhatsAppImage2022-01-18at8.25.21PM.jpeg" alt="image" title=""></p>

<p>Now it's difficult for Naruto to kill him. But then Negi (Naruto's friend) sees Orochimaru's Chakra Network. Chakra Network is like the nervous system, but instead of an electrical pulse, it transmits chakra, a form of energy. </p>

<p>His Chakra network is like a graph of N nodes and E edges. Negi informs naruto that if he stricks on Orochimaru's <strong>Critical Chakra Point</strong>, he will be able to bring him down.</p>

<p><strong>A Critical Chakra Point</strong> is a node that makes the graph disconnected when destroyed.</p>

<p>Your task is to inform the number of the critical chakra points given a graph.</p></div></div></div><div class="challenge_input_format"><div class="msB challenge_input_format_title"><p><strong>Input Format</strong></p></div><div class="msB challenge_input_format_body"><div class="hackdown-content"><p>The input will consist of a series of test cases. Each test case will start with the number N of chakra points, and the number M of bridges between those points. Following there will be M lines each describing a bridge. Each of these M lines will contain two integers Ui, Vi (1 ≤ Ui,Vi ≤ N), indicating that there is a bridge connecting chakra point node Ui and Vi.</p></div></div></div><div class="challenge_constraints"><div class="msB challenge_constraints_title"><p><strong>Constraints</strong></p></div><div class="msB challenge_constraints_body"><div class="hackdown-content"><ul>
<li>1 ≤ N ≤ 10^5</li>
<li>1 ≤ M ≤ 10^5</li>
</ul></div></div></div><div class="challenge_output_format"><div class="msB challenge_output_format_title"><p><strong>Output Format</strong></p></div><div class="msB challenge_output_format_body"><div class="hackdown-content"><p>An integer informing about total number of Critical Chakra Points.</p></div></div></div><div class="challenge_sample_input"><div class="msB challenge_sample_input_title"><p><strong>Sample Input 0</strong></p></div><div class="msB challenge_sample_input_body"><div class="hackdown-content"><div class="highlight"><pre><span></span><span class="err">3 3</span>
<span class="err">1 2</span>
<span class="err">2 3</span>
<span class="err">1 3</span>
</pre></div>
</div></div></div><div class="challenge_sample_output"><div class="msB challenge_sample_output_title"><p><strong>Sample Output 0</strong></p></div><div class="msB challenge_sample_output_body"><div class="hackdown-content"><div class="highlight"><pre><span class="err">0</span>
</pre></div>
</div></div></div><div class="challenge_explanation"><div class="msB challenge_explanation_title"><p><strong>Explanation 0</strong></p></div><div class="msB challenge_explanation_body"><div class="hackdown-content"><p>You can remove any node but the graph will still be connected</p>

<p><img src="https://s3.amazonaws.com/hr-assets/0/1642519572-c4458c5c1c-aaa.png" alt="image" title=""></p></div></div></div><div class="challenge_sample_input"><div class="msB challenge_sample_input_title"><p><strong>Sample Input 1</strong></p></div><div class="msB challenge_sample_input_body"><div class="hackdown-content"><div class="highlight"><pre><span></span><span class="err">6 8</span>
<span class="err">1 3</span>
<span class="err">6 1</span>
<span class="err">6 3</span>
<span class="err">4 1</span>
<span class="err">6 4</span>
<span class="err">5 2</span>
<span class="err">3 2</span>
<span class="err">3 5</span>
</pre></div>
</div></div></div><div class="challenge_sample_output"><div class="msB challenge_sample_output_title"><p><strong>Sample Output 1</strong></p></div><div class="msB challenge_sample_output_body"><div class="hackdown-content"><div class="highlight"><pre><span class="err">1</span>
</pre></div>
</div></div></div><div class="challenge_explanation"><div class="msB challenge_explanation_title"><p><strong>Explanation 1</strong></p></div><div class="msB challenge_explanation_body"><div class="hackdown-content"><p>If we remove node 3 then the graphs becomes disconnected as no path is their for 2 and 5 from 1, 4 and 6.</p>

<p><img src="https://s3.amazonaws.com/hr-assets/0/1642519630-d95c85824a-aaaa.png" alt="image" title=""></p></div></div></div>
            </div></div>
