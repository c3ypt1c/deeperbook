# DeeperBook
The privacy, anti-censorship based social media.

The web is at a true turning point where censorship is the norm of internet. Monopoly and corruption runs the many services on the internet. Not this one. Let the fall of Google, Facebook and YouTube spark a new era of free data.

With the new state-of-the-art encryption and security, you can rest assure that even with a forced physical take over of this website and all of it's hardware, your data and content will remain secure. 

=== How it works ===
<tt>
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
|                                                                        - ■ x|
|                               Simplified Graph                              |
|                                                         _ _ _ _ _ _ _ _ _   |
|         _ _ _ _                                        |            - ■ x|  |
|        |  - ■ x|          (1)                  (2)     |       CA:       |  |
|        |  You  | > > > > > > > > > > > > . > > > > > > |  Let's Encrypt  |  |
|        |_ _ _ _| < < < < < < < < < < < < .             |_ _ _ _ _ _ _ _ _|  |
|                             (5)          ↕                                  |
|             ↕                                                   ↕           |
|                                          ↕                                  |
|             ↕                                                   ↕           |
|         _ _ _ _ _               ~|SSL encryption|~                          |
|        |    - ■ x|                                         (6)  ↕           |
|  (7)   |  Google |                       ↕                                  |
|        |   API   |                           (3)                ↕           |
|        |_ _ _ _ _|                       ↕                                  |
|                                      _ _ _ _ _ _                ↕           |
|             ↕                      |       - ■ x|                           |
|             . > > > > > > > > > >  |    Main    | > > > > > > > .           |
|             . < < < < < < < < < <  |   Server   | < < < < < < < .           |
|                                    |_ _ _ _ _ _ |                           |
|                                           (4)                               |
| _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |

</tt>

1. When you first visit this website, you will query the nearest DNS server about it's IP address.  
2. When you connect to the HTTPS port, your computer will then query the nearest Let's Encrypt Certificate Authority to confirm the certificate provided by my server.
3. You send an encrypted message to a server, a message, let's say. The message travels from your computer to the main server 
4. Your message is decrypted when it arrives and then is encrypted with the state-of-the-art encryption and sent forward to the intended recipient.
5. You receive your message back as a confirmation that the message has been sent.

==Optional Steps==
6. Server automatically updates it's certificates to keep you and other users safe from prying eyes and unauthorized personnel. Thank you so much: Let's Encrypt! (https://letsencrypt.org/)
7. Sometimes, when you or your browser sends too many requests to the main server, a captcha may be required for you to continue. This is to ensure that the server cannot be broken into using brute-force type of attacks. You can choose weather you want your account protected by a captcha. 

=== To do: ===
Key: [ ] To do, [-] In progress, [x] Finished
[-] - Finish Secure Algorithm.
[-] - Finish Database.
[ ] - Create Web Front.
[ ] - Integrate Google Captcha API.
[ ] - Publish.
[ ] - Create my own Captcha to replace reliance on Google.